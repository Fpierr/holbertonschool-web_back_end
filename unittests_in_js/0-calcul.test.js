const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function () {
  it('should return 4 when (1, 3)', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should round 3.7 to 4 and return 5 when (1, 3.7)', function () {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should round 1.2 to 1 and 3.7 to 4, return 5', function () {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should round 1.5 to 2 and 3.7 to 4, return 6', function () {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('should handle negatives: -1.2 rounds to -1 and 3.7 to 4, return 3', function () {
    assert.strictEqual(calculateNumber(-1.2, 3.7), 3);
  });

  it('should handle both negatives: -1.5 rounds to -1 and -3.7 to -4, return -5', function () {
    assert.strictEqual(calculateNumber(-1.5, -3.7), -5);
  });

  it('should return 0 when (0, 0)', function () {
    assert.strictEqual(calculateNumber(0, 0), 0);
  });
});
