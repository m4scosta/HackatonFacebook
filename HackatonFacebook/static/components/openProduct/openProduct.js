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
        controller: function($scope, Ajax) {
            $scope.closeProduct = function(){
                $scope.viewproduct = false;
            };

            $scope.like = function(){
                Ajax.post('/like', angular.toJson({recipe_id: $scope.openproduct.id})).success(function(result){
                    console.log('opa o usuario deu um like');
                }).error(function(){

                });
            };

            $scope.favoritos = function(){
                Ajax.post('/favoritos', angular.toJson({recipe_id: $scope.openproduct.id})).success(function(result){
                    console.log('opa o usuario deu um like');
                }).error(function(){

                });
            };
        }
    }
});

