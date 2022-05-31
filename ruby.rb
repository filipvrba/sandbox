require 'json'

data = %x(trans --words-db get)
json = JSON.parse( data )

json.each do |key, value|
    puts key
end