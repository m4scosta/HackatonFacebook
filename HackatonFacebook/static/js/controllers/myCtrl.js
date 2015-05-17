/**
 * Created by bustamante on 5/15/15.
 */
angular.module('HackathonApp').factory('facebookService', function($q) {
    return {
        getUserData: function() {
            var deferred = $q.defer();
            FB.api('/891817570857458', function(response) {
                if (!response || response.error) {
                    deferred.reject('Error occured');
                } else {
                    deferred.resolve(response);
                }
            });
            return deferred.promise;
        }
    }
});

angular.module('HackathonApp').controller('MyCtrl', function(Ajax, $scope, $window, facebookService){

	$window.fbAsyncInit = function() {
        FB.init({ 
          appId: '1584090185178966',
          status: true, 
          cookie: true, 
          xfbml: true,
          version: 'v2.3'
        });

        FB.getLoginStatus(function(response) {
		    facebookService.getUserData().then(function(response) {
	       		$window.user = response;
	    	});
		});
    };

});
