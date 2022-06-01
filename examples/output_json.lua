json = require "../thirdside/json"

function get_json( message )
    data = io.popen( message )
    result = data:read("*a" )
    data:close()
    return json.decode(result)
end

data = get_json("trans --words-db get")
for key, value in pairs(data) do
    print( string.format("%s - %s", key, value) )
end