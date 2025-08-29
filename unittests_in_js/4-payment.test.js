const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');
const { expect } = require('chai');

describe('sendPaymentRequestToApi with stub', function () {
  it('should stub Utils.calculateNumber and verify console.log', function () {
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);

    const logSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    expect(stub.calledOnce).to.be.true;
    expect(stub.calledWith('SUM', 100, 20)).to.be.true;

    expect(logSpy.calledOnce).to.be.true;
    expect(logSpy.calledWith('The total is: 10')).to.be.true;

    stub.restore();
    logSpy.restore();
  });
});
