var request = require('superagent');
var expect = require('expect.js');

describe('**************** Flask tests ***************', function() {
  before(function(done){

    done();
  });

  describe('Checking the resume route isn\'t missing', function(){
    it('check resume route exists', function(done){
      request.get('localhost:5000/resume').end(function(err, res){
        expect(res).to.exist;
        done();
      });
    });
  });

  describe('Checking the flask endpoint', function(){
    it('check resume route exists', function(done){
      request.get('localhost:5000/flask').end(function(err, res){
        expect(res).to.exist;
        done();
      });
    });
  });
});
