-- split-merged-cells.lua
-- Use to_simple_table approach to properly preserve cell content

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
    io.stderr:write("DEBUG: Processing table with " .. #tbl.bodies .. " bodies\n")
    
    -- Convert to simple table format to avoid AST structure issues
    local simple_table = utils.to_simple_table(tbl)
    
    io.stderr:write("DEBUG: Converted to simple table - Header cells: " .. #simple_table.header .. ", Data rows: " .. #simple_table.rows .. "\n")
    
    -- Flatten cell content: Convert multiple Para blocks to single Plain with <br>
    for i, header_cell in ipairs(simple_table.header) do
        simple_table.header[i] = flatten_cell_content(header_cell)
        local content = utils.stringify(simple_table.header[i])
        io.stderr:write("DEBUG: Header[" .. i .. "] flattened = '" .. content .. "'\n")
    end
    
    for row_idx, row in ipairs(simple_table.rows) do
        for cell_idx, cell in ipairs(row) do
            simple_table.rows[row_idx][cell_idx] = flatten_cell_content(cell)
            local content = utils.stringify(simple_table.rows[row_idx][cell_idx])
            io.stderr:write("DEBUG: Row[" .. row_idx .. "][" .. cell_idx .. "] flattened = '" .. content .. "'\n")
        end
    end
    
    -- Convert back from simple table to regular table
    local new_table = utils.from_simple_table(simple_table)
    
    -- Create proper colspecs instead of removing them entirely
    -- Number of columns = number of header cells
    local num_cols = #simple_table.header
    local new_colspecs = {}
    
    for i = 1, num_cols do
        -- Create ColSpec with default alignment and no width constraint
        table.insert(new_colspecs, {pandoc.AlignDefault, nil})
    end
    
    new_table.colspecs = new_colspecs
    
    io.stderr:write("DEBUG: Converted back to regular table, created " .. num_cols .. " colspecs\n")
    
    return new_table
end