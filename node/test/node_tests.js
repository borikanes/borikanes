var request = require('superagent');
var expect = require('expect.js');

describe('**************** Node tests ***************', function() {
  before(function(done){
    //nothing so far
    done();
  });

  describe('Just sanity check to see that root path exists', function(){
    it('check root(/) exists', function(done){
      request.get('localhost:8080').end(function(err, res){
        expect(res).to.exist;
        done();
      });
    });

    it('check /hello exists', function(done){
      request.get('localhost:8080/hello').end(function(err, res){
        expect(res).to.exist;
        expect(res.body).to.not.contain("Cannot GET");
        expect(res.body.message).to.contain("welcome");
        done();
      });
    });
  });

});
