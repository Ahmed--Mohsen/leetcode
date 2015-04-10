def swap(a, b):
	a = a + b
	b = a - b
	a = a - b
	print a, b
	
def swap_xor(a, b):
	a = a ^ b
	b = a ^ b
	a = a ^ b
	print a, b
	
def get_max(a, b):
	c = a - b
	k = (c >> 31) & 1
	max = a - k * c
	print c,k
	return max
	
def twos_count(N):
	int numToRight=0, count=0, i=1;
	int pow10=1; // speed up power calculation
	while(N/10){
	    int digit = N % 10;
	    if (digit == 1){
	        count += digit*i*pow10;
	    } else if (digit == 2){
	        count += digit*i*pow10 + numToRight+1;
	    } else {
	        count += digit*i*pow10 + numToRight+pow10;
	    }
	    numToRight += digit*pow10;
	    N /=10;
	    pow10 *=10;
	    i++;
	}
	
#swap_xor(2,5)
print get_max(3,12)