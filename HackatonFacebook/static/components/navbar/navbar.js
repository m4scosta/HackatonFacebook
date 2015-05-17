/**
 * Created by bustamante on 5/16/15.
 */

angular.module('HackathonApp').directive('navbarHack', function(){
    return {
        restrict: 'E',
        templateUrl: 'static/components/navbar/navbar.html',
        controller: function($scope, $window, facebookService){
        	$scope.getData = function() {
	    		facebookService.getUserData().then(function(response) {
		       		window.user = $scope.user = response;
		    	});
        	};

        	$scope.$watch(function(){
        		return $window.user
        	}, function(){
        		if(FB !== undefined)
        			$scope.getData();
        	});
        }
    }
});
