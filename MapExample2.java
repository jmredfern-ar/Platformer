import java.util.HashMap;
import java.util.Map;

public class MapExample2 {
	
	// Collections based on hashing calculate the hash value for a given key 
	// (using the hashCode() method) and use this value internally to store the data 
	// – so that access operations are much more efficient.
	private static Map<String, String> partsInventory = new HashMap<String, String>();
	
	public static void main(String[] args) {
		
		// LOAD K/V PAIRS INTO MAP
		partsInventory.put("1003", "Bulb");
		partsInventory.put("10431169", "Starter DT466E");
		partsInventory.put("15W40", "OIL, Engine");
		partsInventory.put("1819391C2", "BELT, FAN DT 466E");
		
		// GET VALUE USING KEY
		System.out.println(partsInventory.get("15W40") + "\n");
		
		// ITERATE AND PRINT MAP
		for(Map.Entry<String, String> pi : partsInventory.entrySet()) {
			System.out.println("Key: " + pi.getKey() + " | Value: " + pi.getValue());
		}
		System.out.println();
		
		// CHANGING A VALUE
		partsInventory.put("1003", null);
		System.out.println("Key: 1003 | Value: " + partsInventory.get("1003") + "\n");
		
		// REPRINTING THE MAP USING A FUNCTION
		printMap(partsInventory);
	}
	
	// FUNCTION TO PRINT MAP of <String, String>
	public static void printMap(Map<String, String> map) {
		for(Map.Entry<String, String> mapEntry : map.entrySet()) {
			System.out.println("Key: " + mapEntry.getKey() + " | Value: " + mapEntry.getValue());
		}
		System.out.println();
	}
}
