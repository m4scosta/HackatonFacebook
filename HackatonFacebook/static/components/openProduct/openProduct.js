/**
 * Created by bustamante on 5/16/15.
 */

angular.module('HackathonApp').directive("openProduct", function(){
    return {
        restrict: 'E',
        scope: {
            product: '=',
            viewproduct: '=',
            openproduct: '='
        },
        templateUrl: 'static/components/openProduct/openProduct.html',
        controller: function($scope) {
            $scope.closeProduct = function(){
                $scope.viewproduct = false;
            }
        }
    }
});

