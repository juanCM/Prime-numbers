num_serie = 4;
def get_serie(n):
	for i in range(0,n-1):
		global num_serie, number;
		#print (num_serie);
		num_serie = pow(num_serie,2)-2;
		if(num_serie > number):
			num_serie = num_serie%number;
	return num_serie;
n = 44497;
number = pow(2,n)-1;
ser = get_serie(n-1);
if ser%number == 0:
	print("PRIME");
	print (number);
else:
	print("NO");