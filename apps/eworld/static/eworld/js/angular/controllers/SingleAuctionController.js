/**
 * Created by PerminovMA@live.ru on 27.09.15.
 */


app.controller("SingleAuctionController",
    function ($scope, AuctionsService, $modal, URLs) {
        $scope.updateBets = function () {
            AuctionsService.get_best_bets(
                {
                    auction_id: AUCTION_ID  // variable AUCTION_ID is taken from HTML template
                },
                function (data) {
                    $scope.best_bet = false;
                    $scope.bets = false;
                    if (data.length > 0) {
                        $scope.best_bet = data[0];
                        data.shift();
                        if (data.length > 0) {
                            $scope.bets = data;
                        }
                    }
                },
                function (err_obj) {
                    alert("Произошла ошибка при получении списка ставок, обратитесь к администратору сайта.")
                }
            );
        };
        $scope.updateBets();
        $scope.open_to_bet_modal = function () {
            var modalInstance = $modal.open({
                templateUrl: URLs.to_bet_url,
                controller: 'ToBetController'
            });
        }
    }
);

app.controller(
    "ToBetController",
    function ($scope, $http, $modalInstance, URLs) {
        $scope.submit = function () {
            alert("submit");
        };

        $scope.cancel = function () {
            $modalInstance.dismiss('cancel');
        };
    });