var request = require('superagent');
var expect = require('expect.js');

describe('**************** Flask tests ***************', function() {
  before(function(done){

    done();
  });

  describe('Just sanity check to see that root path exists', function(){
    it('check resume route exists', function(done){
      request.get('localhost:5000/resume').end(function(err, res){
        expect(res).to.exist;
        done();
    });
  });
});
});
