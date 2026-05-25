const Ajv = require('ajv');
const fs = require('fs');

const ajv = new Ajv();
const schema = JSON.parse(fs.readFileSync('schema.json', 'utf8'));
const config = JSON.parse(fs.readFileSync('config.json', 'utf8'));

const validate = ajv.compile(schema);
const valid = validate(config);

if (valid) {
  console.log('✓ Validation passed');
  console.log('Config:', JSON.stringify(config, null, 2));
} else {
  console.log('✗ Validation failed');
  console.log('Errors:', validate.errors);
  process.exit(1);
}
