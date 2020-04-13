/*
By: Ahmed Moustafa (a.k.a geekahmed)
Email: geekahmed1@gmail.com
linkedIn: https://www.linkedin.com/in/geekahmed
*/

public class Codec {
    final String PREFIX = "http://tinyurl.com/";
    final Map<String, String> map = new HashMap<>(); 

    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        final String key = PREFIX + (map.size() + 1);
        map.put(key, longUrl);
        return key;
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        return map.get(shortUrl);
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));
