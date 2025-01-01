function b2alias
    if test -e Jamfile
        string match -g -r "alias\s+(\w+)" < Jamfile
    end
end
