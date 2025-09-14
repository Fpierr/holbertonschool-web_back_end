const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
  const url = 'http://localhost:7865/';

  it('Correct status code?', (done) => {
    request.get(url, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct result?', (done) => {
    request.get(url, (err, res, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('Other? check content-type', (done) => {
    request.get(url, (err, res, body) => {
      expect(res.headers['content-type']).to.include('text/html');
      done();
    });
  });
});
