/**
 * Created by bustamante on 5/16/15.
 */

angular.module('HackathonApp').directive("tagsHack", function(){
    return {
        restrict: 'E',
        scope: {
            ingredients: '=',
            msg: '@?',
            btnlg: '@?'
        },
        templateUrl: 'static/components/tags/tags.html',
        controller: function($scope) {
            $scope.toggleVisibility = function (index) {
                $scope.ingredients[index].delete = !$scope.ingredients[index].delete;
            };

            $scope.takeOff = function (index) {
                $scope.ingredients.splice(index, 1);
            };
        }
    }
});

