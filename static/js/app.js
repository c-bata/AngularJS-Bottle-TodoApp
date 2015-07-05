p.list = function(callback){
    this.$http({
        method: 'GET',
        url   : '/api/tasks',
        params: {
            method: 'list'
        }
    }).success(function(response){
        callback.call(this, response.data)
    });
};