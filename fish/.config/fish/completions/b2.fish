function b2alias
    if not test -e Jamfile
        return 1
    end

    set -l targets (string match -g -r "(alias|lib|exe)\s+(\w+)" < Jamfile)

    for i in (seq 1 2 (count $targets))
        printf '%s\t%s\n' $targets[(math $i + 1)] $targets[$i]
    end
end

complete --exclusive b2 -a '(b2alias)'
