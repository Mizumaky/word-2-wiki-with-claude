-- split-merged-cells.lua
-- Use to_simple_table approach to properly preserve cell content

local utils = require 'pandoc.utils'

function Table(tbl)
    io.stderr:write("DEBUG: Processing table with " .. #tbl.bodies .. " bodies\n")
    
    -- Convert to simple table format to avoid AST structure issues
    local simple_table = utils.to_simple_table(tbl)
    
    io.stderr:write("DEBUG: Converted to simple table - Header cells: " .. #simple_table.header .. ", Data rows: " .. #simple_table.rows .. "\n")
    
    -- Debug: Print all content to verify it's preserved
    for i, header_cell in ipairs(simple_table.header) do
        local content = utils.stringify(header_cell)
        io.stderr:write("DEBUG: Header[" .. i .. "] = '" .. content .. "'\n")
    end
    
    for row_idx, row in ipairs(simple_table.rows) do
        for cell_idx, cell in ipairs(row) do
            local content = utils.stringify(cell)
            io.stderr:write("DEBUG: Row[" .. row_idx .. "][" .. cell_idx .. "] = '" .. content .. "'\n")
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