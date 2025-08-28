-- table-pipe-converter.lua
-- Converts complex Word tables to Obsidian-compatible pipe tables
-- Flattens multi-paragraph cells using <br> separators to satisfy Pandoc's "simple table" criteria

local utils = require 'pandoc.utils'

function flatten_cell_content(cell)
    -- Convert cell with multiple Para blocks to single Plain block with <br> separators
    if not cell or #cell == 0 then
        return cell
    end
    
    local inlines = {}
    
    for i, block in ipairs(cell) do
        if block.tag == "Para" then
            -- Add paragraph content
            for _, inline in ipairs(block.content) do
                table.insert(inlines, inline)
            end
            -- Add <br> separator between paragraphs (except after the last one)
            if i < #cell then
                table.insert(inlines, pandoc.RawInline("html", "<br>"))
            end
        elseif block.tag == "Plain" then
            -- Add plain content
            for _, inline in ipairs(block.content) do
                table.insert(inlines, inline)
            end
            -- Add <br> separator between blocks (except after the last one)
            if i < #cell then
                table.insert(inlines, pandoc.RawInline("html", "<br>"))
            end
        else
            -- For other block types, convert to plain text and add
            local text = utils.stringify(block)
            if text ~= "" then
                table.insert(inlines, pandoc.Str(text))
                -- Add <br> separator between blocks (except after the last one)
                if i < #cell then
                    table.insert(inlines, pandoc.RawInline("html", "<br>"))
                end
            end
        end
    end
    
    -- Return single Plain block with all content
    return {pandoc.Plain(inlines)}
end

function Table(tbl)
    -- Convert to simple table format for easier processing
    local simple_table = utils.to_simple_table(tbl)
    
    -- Flatten cell content: Convert multiple Para blocks to single Plain with <br>
    -- This makes tables "simple" enough for Pandoc to output as pipe tables
    for i, header_cell in ipairs(simple_table.header) do
        simple_table.header[i] = flatten_cell_content(header_cell)
    end
    
    for row_idx, row in ipairs(simple_table.rows) do
        for cell_idx, cell in ipairs(row) do
            simple_table.rows[row_idx][cell_idx] = flatten_cell_content(cell)
        end
    end
    
    -- Convert back to regular table format
    local new_table = utils.from_simple_table(simple_table)
    
    -- Create proper colspecs with default alignment (required for content preservation)
    local num_cols = #simple_table.header
    local new_colspecs = {}
    
    for i = 1, num_cols do
        table.insert(new_colspecs, {pandoc.AlignDefault, nil})
    end
    
    new_table.colspecs = new_colspecs
    
    return new_table
end