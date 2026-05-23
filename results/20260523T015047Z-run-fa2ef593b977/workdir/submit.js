// Submit form signup-2026 with the three required fields
const form_id = "signup-2026";
const fields = [
  { name: "email", value: "alice@example.com" },
  { name: "full_name", value: "Alice Example" },
  { name: "age", value: "30" }
];

// Output the call for verification
console.log(JSON.stringify({ function: "submit_form", arguments: { form_id, fields } }, null, 2));
