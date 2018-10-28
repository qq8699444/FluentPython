import  array

symbols = "$#$%^&"
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

codes = [ord(symbol) for symbol in symbols]
print(codes)

beyond_codes = [ord(symbol) for symbol in symbols if ord(symbol)<50]
print(beyond_codes)

beyond_codes = list(filter(lambda c:c < 50,map(ord,symbols)))
print(beyond_codes)

colors = ['black','white']
sizes = ['S','M','L']
tshirts = [(color,size) for color in colors for size in sizes]
print(tshirts)

print("#################################################")

codes = tuple(ord(symbol) for symbol in symbols)
print(codes)

codes = array.array('I',(ord(symbol) for symbol in symbols))
print(codes)

##

##use ssh connection
