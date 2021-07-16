# speed test is library used to measure our current state of internet speed
from speedtest import Speedtest

# creating instance of Speedtest
st=Speedtest()

print("checking your internet speed .......")
# checking download speed of our internet connection
d=st.download()

# checkin upload speed of out internet connection
u=st.upload()

print("your download speed is ... ",d," Kb/s")
print("your upload speed is ... ",u," Kb/s")

print("your download speed is ... ",(d/10**6)/7," MB/s")
print("your upload speed is ... ",(u/10**6)/7," MB/s")

print("your download speed is ... ",(d/10**6)," Mb/s")
print("your upload speed is ... ",(u/10**6)," Mb/s")
ping=st.results.ping
print("your ping is .. ",ping, " milliseconds")

a=int(input("want to download or upload any file? choose - 1.download  2.upload           "))
b=int(input("file in .. 1. MB 2. KB 3. Mb          "))
c=int(input("size of file ...            "))

s=d if a==1 else u
if b==1 :
    s=(s/10**6)/7
elif b==2 :
    s=s
else :
    s=s/10**6

print("Approx Time take ...",c/s,"seconds")