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

                    // calculation of the new price
                    var current_best_price = $scope.best_bet ? $scope.best_bet.amount : START_PRICE;
                    if (current_best_price - STANDARD_DECREASE_RATE < MIN_PRICE) {
                        $scope.decrease_rate = current_best_price - MIN_PRICE;
                    }
                    else {
                        $scope.decrease_rate = STANDARD_DECREASE_RATE;
                    }
                    $scope.new_amount = current_best_price - $scope.decrease_rate;
                    //
                },
                function (err_obj) {
                    console.log(err_obj);
                    alert("Произошла ошибка при получении списка ставок, обратитесь к администратору сайта.")
                }
            );
        };

        $scope.updateComments = function () {
            AuctionsService.get_comments(
                {
                    auction_id: AUCTION_ID
                },
                function (data) {
                    $scope.comments = data;
                },
                function (err_obj) {
                    console.log(err_obj);
                    alert("Произошла ошибка при получении комментариев, обратитесь к администратору сайта.")
                }
            );
        };

        $scope.updateBets();
        $scope.updateComments();

        $scope.to_bet = function () {
            AuctionsService.to_bet(
                {
                    id: AUCTION_ID,  // variable AUCTION_ID is taken from HTML template
                    amount: $scope.new_amount
                },
                function (data) {
                    console.log(data);
                    $scope.updateBets();
                },
                function (err_obj) {
                    console.log(err_obj);
                    alert("Произошла ошибка. Обновите страницу и попробуйте снова.")
                }
            );

        };
    }
);