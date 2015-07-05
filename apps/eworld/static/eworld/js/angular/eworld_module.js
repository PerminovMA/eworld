/**
 * Created by PerminovMA@live.ru on 26.06.15.
 */

var app = angular.module('eworld_base_module', []);

app.config(function ($interpolateProvider, $httpProvider) {
    //allow django templates and angular to co-exist
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
});

app.controller(
    "AuthorizationController",
    function ($scope, $http) {
        $scope.namee = "Mihail";

        $scope.testFunction = function () {
            alert("asd");
        }

        $scope.submit = function () {

            //alert($scope.email + " " + $scope.password);

            //$httpProvider.defaults.xsrfCookieName = 'csrftoken';
            //$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

            $http({method: "POST", url: "profile/authorization"}).
                success(function (data, status) {
                    $scope.status = status;
                    $scope.data = data;
                    console.log("SUCCESS");
                    alert(status + " " + data);
                }).
                error(function (data, status) {
                    $scope.data = data || "Request failed";
                    $scope.status = status;
                    console.log("ERROR");
                    alert(status + " " + data);
                });
        };
    });


// URLs config
//app.constant("urls", {edit_campaign_url: "/control_panel/edit_campaign/"});