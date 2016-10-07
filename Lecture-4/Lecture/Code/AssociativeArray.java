import java.util.HashMap; // or TreeMap

// mapping key: String to value: Integer
HashMap<String, Integer> age = new HashMap<>();

if (age.containsKey("Frank")) // check for key
	age.remove("Frank"); // deletes a mapping

age.put("Bob", 20); // insert entry

System.@{\textbf{\textit{\color{java_static}out}}}@.printf("Bob is %d years old",
	// retrieves a value for key "Bob"
	age.get("Bob"));