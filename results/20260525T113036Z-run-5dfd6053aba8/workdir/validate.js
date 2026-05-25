const Ajv = require('ajv');
const fs = require('fs');

const ajv = new Ajv();
const schema = JSON.parse(fs.readFileSync('./schema.json', 'utf8'));
const config = JSON.parse(fs.readFileSync('./config.json', 'utf8'));

const validate = ajv.compile(schema);
const valid = validate(config);

if (valid) {
  console.log('✓ config.json validates successfully against schema.json');
  process.exit(0);
} else {
  console.log('✗ Validation errors:');
  console.log(JSON.stringify(validate.errors, null, 2));
  process.exit(1);
}
