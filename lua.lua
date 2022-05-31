function json( message )
    data = io.popen( message )
    result = data:read("*a")
    data:close()
    return result
end

print (json( 'trans --words-db get' ))