import sys
import antigravity

def main():
    try:
        if len(sys.argv) != 4:
            raise ValueError("Usage: geohashing.py <latitude> <longitude> <date as YYYY-MM-DD>")
        
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        date = sys.argv[3]
        
        antigravity.geohash(latitude, longitude, date.encode('utf-8'))
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
