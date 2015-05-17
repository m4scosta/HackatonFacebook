/**
 * Created by bustamante on 5/16/15.
 */

angular.module('HackathonApp').directive("firstSearch", function(){
    return {
        restrict: 'E',
        scope: {
            ingredients: '=',
            recipe: '=',
            small: '='
        },
        templateUrl: 'static/components/firstSearch/firstSearch.html',
        controller: function($scope, Ajax) {
            $scope.newIngredient = function () {
                if ($scope.ingerdientModel !== undefined && $scope.ingerdientModel != '') {
                    if (!window.has_attr('name', $scope.ingerdientModel, $scope.ingredients)) {
                        $scope.ingredients.push({name: $scope.ingerdientModel});
                    }
                    $scope.ingerdientModel = ''
                }
            };

            $scope.toggleVisibility = function (index) {
                $scope.ingredients[index].delete = !$scope.ingredients[index].delete;
            };

            $scope.takeOff = function (index) {
                $scope.ingredients.splice(index, 1);
            };

            $scope.search = function () {
                $scope.have_search = $scope.small = true;
                var send = {ingredients: []};
                for (var i = 0; i < $scope.ingredients.length; ++i)
                    send.ingredients.push($scope.ingredients[i].name);

                if (send.ingredients.length > 0) {
                    Ajax.post('/list/receipe', angular.toJson(send)).success(function (result) {
                        $scope.have_search = true;
                    }).error(function (result) {

                    });
                }
            }
        }
    }
});

