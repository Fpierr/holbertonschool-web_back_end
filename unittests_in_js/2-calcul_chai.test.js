const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', function () {
  describe('SUM', function () {
    it('should add two rounded numbers correctly', function () {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('should handle rounding up', function () {
      expect(calculateNumber('SUM', 1.6, 3.6)).to.equal(6);
    });

    it('should handle negatives', function () {
      expect(calculateNumber('SUM', -1.4, -3.6)).to.equal(-5);
    });
  });

  describe('SUBTRACT', function () {
    it('should subtract two rounded numbers correctly', function () {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('should handle rounding both up', function () {
      expect(calculateNumber('SUBTRACT', 2.6, 1.6)).to.equal(1);
    });

    it('should handle negatives', function () {
      expect(calculateNumber('SUBTRACT', -1.4, -3.6)).to.equal(3);
    });
  });

  describe('DIVIDE', function () {
    it('should divide two rounded numbers correctly', function () {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('should return Error when dividing by 0', function () {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });

    it('should handle negatives', function () {
      expect(calculateNumber('DIVIDE', -3.7, 1.2)).to.equal(-4);
    });
  });
});
