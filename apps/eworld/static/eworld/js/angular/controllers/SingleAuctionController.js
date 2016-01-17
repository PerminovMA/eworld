/**
 * Created by PerminovMA@live.ru on 27.09.15.
 */


app.controller("SingleAuctionController",
    function ($scope, AuctionsService, $modal, URLs, $interval) {
        var update_bets_timer;
        var update_comments_timer;

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
                    $scope.auction_is_stopped = $scope.decrease_rate <= 0;

                    // bet reached a minimum, the auction is stopped. Stops timers
                    if ($scope.auction_is_stopped) {
                        if (angular.isDefined(update_bets_timer)) {
                            $interval.cancel(update_bets_timer);
                            update_bets_timer = undefined;
                        }
                        if (angular.isDefined(update_comments_timer)) {
                            $interval.cancel(update_comments_timer);
                            update_comments_timer = undefined;
                        }
                    }

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
                    alert("Произошла ошибка. Обновите страницу и попробуйте снова.");
                }
            );

        };

        $scope.make_comment = function () {
            if (!this.new_comment_text) {
                alert("Введите текст.");
                return;
            }

            AuctionsService.make_comment(
                {
                    id: AUCTION_ID,  // variable AUCTION_ID is taken from HTML template
                    text: this.new_comment_text
                },
                function (data) {
                    if (data.result != "success") {
                        alert("Произошла ошибка при отправке комментария: " + data.message);
                    }
                    $scope.updateComments();
                },
                function (err_obj) {
                    console.log(err_obj);
                    alert("Произошла ошибка при отправке комментария: " + err_obj);
                }
            );
            this.new_comment_text = '';
        };

        if (!$scope.auction_is_stopped && !angular.isDefined(update_bets_timer)) {
            update_bets_timer = $interval($scope.updateBets, 1000);
        }
        if (!$scope.auction_is_stopped && !angular.isDefined(update_comments_timer)) {
            update_comments_timer = $interval($scope.updateComments, 2000);
        }

    }
);