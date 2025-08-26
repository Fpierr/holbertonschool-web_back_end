const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', function () {
    describe('SUM', function () {
        it('sould add two rounded numbers correctly', function () {
            assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
        });

        it('should handle rounding up', function() {
            assert.strictEqual(calculateNumber('SUM', 1.6, 3.6), 6);
        });

        it('should handle negatives', function () {
            assert.strictEqual(calculateNumber('SUM', -1.4, -3.6), -5);
        });
    });

    describe('SUBTRACT', function () {
        it('should subtract two rounded numbers correctly', function () {
            assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
        });

        it('should handle rounding both up', function () {
            assert.strictEqual(calculateNumber('SUBTRACT', 2.6, 1.6), 1);
        });

        it('should handle negatives', function () {
            assert.strictEqual(calculateNumber('SUBTRACT', -1.4, -3.6), 3);
        });
    });

    describe('DIVIDE', function () {
        it('should divide two rounded numbers correctly', function () {
            assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
        });

        it('should return Error when dividing by 0', function () {
            assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
        });

        it('should handle negatives', function () {
            assert.strictEqual(calculateNumber('DIVIDE', -3.7, 1.2), -4);
        });
    });
});
