import sys

def si(p,t,r):
    return (p*t*r)/100

if __name__ == "__main__":
    if len(sys.argv)==3:
        p = float(sys.argv[1])
        t = float(sys.argv[2])
        r = float(sys.argv[3])
        
    else:
        p = 100
        t = 1
        r = 5
print(f"Simple Interest is: {si(p,t,r)}")        