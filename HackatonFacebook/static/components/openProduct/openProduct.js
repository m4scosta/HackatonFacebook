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
        controller: function($scope, Ajax, $window) {
            $scope.closeProduct = function(){
                $scope.viewproduct = false;
            };

            $scope.like = function(){
                Ajax.post('/like', angular.toJson({recipe_id: $scope.openproduct.id})).success(function(result){
                    $scope.openproduct.likes += 1;
                }).error(function(){
                    alert('Você já curtiu essa receita');
                });
            };

            $scope.favoritos = function(){
                Ajax.post('/favoritos', angular.toJson({recipe_id: $scope.openproduct.id})).success(function(result){
                    $scope.openproduct.favorites += 1;
                }).error(function(){
                    alert('Essa receita já está em seus favoritos.');
                });
            };

            $scope.imp = function(){
                $window.location.href='/imprimir/'+ $scope.openproduct.id + '/?q=' + $scope.openproduct.ingredients_out;
            };

            $scope.publishRecipe = function() {

                if ($window.FB != undefined) {

                    $window.FB.getLoginStatus(function (response) {
                        if (response.status === "connected") {

                            body = "Ola pessoal quero fazer a receita " + $scope.openproduct.name + ".\n" +
                                "Mas me faltam alguns ingredientes, alguem gostaria de " +
                                "se juntar a mim e trazer o que falta?\n\n" + $scope.openproduct.ingredients_out.join("\n");

                            $window.FB.api("/me/feed", "post", {message: body}, function (response) {
                                if (!response || response.error) {
                                    alert("Nao foi possivel postar, tente novamente.");
                                } else {
                                    alert("Postado com sucesso na sua timeline");
                                }
                            });

                        } else {
                            FB.login(function(response) {}, {
                               scope: 'publish_actions', 
                               return_scopes: true
                            });
                        }
                    });

                }
            };
        }
    }
});

