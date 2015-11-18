/**
 * Created by PerminovMA@live.ru on 27.09.15.
 */


app.controller("SingleAuctionController",
    function ($scope, BetsService) {
        $scope.updateBets = function () {
            BetsService.query(
                {
                    auction_id: AUCTION_ID  // variable AUCTION_ID is taken from HTML template
                },
                function (data) {
                    $scope.best_bet = NaN;
                    $scope.bets = NaN;
                    if (data.length > 0) {
                        $scope.best_bet = data[0];
                        data.shift();
                        if (data.length > 0) {
                            $scope.bets = data;
                        }
                    }
                    console.log($scope.best_bet.owner.user.avatar);
                },
                function (err_obj) {
                    alert("Произошла ошибка при получении списка ставок, обратитесь к администратору сайта.")
                }
            );
        };
        $scope.updateBets();
    }
);