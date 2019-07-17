// Call API to fetch cart count
function getCartItemsCount() {
    var count = 0;
    $.get('http://127.0.0.1:8000/cart/count/', function(data, status) {
        $('#cart-badge').html(data.count);
    });
}

// Add to cart
function getCartBadgeCount() {
    return parseInt(document.getElementById('cart-badge').textContent);
}

function cart(itemId) {
    var quantity = $('#quantity-' + itemId).val();
    $.ajax({
        url: `http://127.0.0.1:8000/cart/${itemId}/${quantity}/`,
        success: function() {
            document.getElementById('cart-badge').innerHTML = getCartBadgeCount() + parseInt(quantity);
        }
    });
}

function createItemSmDetailElement(id, title, image, price, slug, date) {
    var url = 'http://127.0.0.1:8000';
    return `<div class="card mb-3">
                <div class="row no-gutters">
                    <div class="col-md-4">
                        <img src="${url}/media/${image}" class="card-img">
                    </div>

                    <div class="col-md-8">
                        <div class="card-body">
                            <h6 class="card-title">
                                <a href="${url}/items/${id}/${slug}/">${title}</a>
                            </h6>
                            
                            <h6><b>${price}</b></h6>
                        </div>
                    </div>
                </div>
            </div>`;
}

// Search
function search() {
    var searchInput = $('#nav-search').val();
    var searchResultContainer = $('#search-results');
    var noResultsContainer = $('#no-results');
    noResultsContainer.hide();
    if (searchInput.length > 1) {
        var searchSpinner = $('#search-spinner');
        searchSpinner.toggle();
        $.ajax({
            url: `http://127.0.0.1:8000/search/${searchInput}/`,
            success: function(data, status) {
                searchResultContainer.toggle();

                var searchResultItems = $('#search-items');
                searchResultItems.empty();

                searchSpinner.toggle();
                if (data.length === 0) {
                    noResultsContainer.show();
                    console.log('no results found');
                } else {
                    var item;
                    for (var i = 0; i < data.length; i++) {
                        item = data[i];
                        searchResultItems.append(createItemSmDetailElement(item.id, item.title, item.image, item.price, item.slug, item.date));
                    }
                }
            }
        });
    }
}