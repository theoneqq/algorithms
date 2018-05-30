--ignore annotations
local _M = {}
function _M:main(file_name)
    local file = io.input(file_name)
    local words = {}
    repeat
        local line = io.read()
        if not line then break end
        for word in string.gmatch(line, '%w+') do
            table.insert(words, word)
        end
    until false    

    local file_string = table.concat(words)
    local switch_begin_pos, swtich_end_pos = 1, 1
    repeat
        switch_begin_pos = string.find(file_string, 'switch', switch_begin_pos) + 1
        local l, r = 0, 0
        for switch_end_pos = switch_begin_pos, #file_string do
            if string.sub(i, i + 1) == '{' then l = l + 1
            elseif string.sub(i, i + 1) == '}' then r = r + 1 end            
            if l == r then break end
        end
        if string.sub(file_string, switch_end_pos) ~= '}' then break end
        local switch_block = string.sub(file_string, switch_begin_pos, switch_end_pos)
        self:check(switch_block)
    until not switch_begin_pos
end

function _M:check(switch_block)
end
return _M
