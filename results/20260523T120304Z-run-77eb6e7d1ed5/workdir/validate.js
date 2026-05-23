const Ajv = require('ajv');
const fs = require('fs');

const manifest = JSON.parse(fs.readFileSync('./manifest.json', 'utf8'));
const schema = JSON.parse(fs.readFileSync('./schema.json', 'utf8'));

const ajv = new Ajv();
const validate = ajv.compile(schema);
const valid = validate(manifest);

if (valid) {
  console.log('✓ manifest.json is valid against schema.json');
  process.exit(0);
} else {
  console.log('✗ Validation failed:');
  console.log(validate.errors);
  process.exit(1);
}
