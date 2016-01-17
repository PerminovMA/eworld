/**
 * Created by PerminovMA@live.ru on 01.08.15.
 */

app.factory('OrdersService', [
    '$resource', 'URLs', function($resource, URLs) {
        return $resource(URLs.orders_data_url, {}, {
            get_comments: {method:'GET', url:URLs.orders_data_url+':order_id/comments/', isArray:true},
            make_comment: {method:'PUT', params:{order_id: '@id', text: '@text'}, url:URLs.orders_data_url+':order_id/make_comment/'},
        });
    }
]);

app.factory('AuctionsService', [
    '$resource', 'URLs', function($resource, URLs) {
        return $resource(URLs.auctions_data_url, {}, {
            to_bet: {method:'PUT', params:{auction_id: '@id'}, url:URLs.auctions_data_url+':auction_id/to_bet/'},
            make_comment: {method:'PUT', params:{auction_id: '@id', text: '@text'}, url:URLs.auctions_data_url+':auction_id/make_comment/'},
            get_best_bets: {method:'GET', url:URLs.auctions_data_url+':auction_id/best_bets/', isArray:true},
            get_comments: {method:'GET', url:URLs.auctions_data_url+':auction_id/comments/', isArray:true}
        });
    }
]);

app.factory('CategoriesService', [
    '$resource', 'URLs', function($resource, URLs) {
        return $resource(URLs.categories_data_url, {});
    }
]);
