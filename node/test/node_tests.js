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
  });

});
