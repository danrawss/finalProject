document.addEventListener("DOMContentLoaded", () => {
    // Initialize autocomplete functionality
    const searchInput = document.getElementById("search-bar");
    autocomplete(searchInput);

    // Add event listeners for cart operations
    setupCartEventListeners();

    // Add event listeners for wishlist operations
    setupWishlistEventListeners();

    // Add event listener for placing orders
    setupOrderEventListener();
});

/**
 * Set up event listeners for adding/removing items in the shopping cart.
 */
function setupCartEventListeners() {
    // Add to cart functionality
    const addToCartButtons = document.querySelectorAll(".add-to-cart-btn");
    addToCartButtons.forEach(button => {
        button.addEventListener("click", () => {
            const productId = button.getAttribute("data-product-id");

            fetch("/cart/add", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ product_id: productId, quantity: 1 })
            })
                .then(response => response.json())
                .then(data => {
                    if (data.message) {
                        showToast(data.message);
                        updateCartCount(data.total_items);
                    }
                })
                .catch(error => console.error("Error adding item to cart:", error));
        });
    });

    // Remove from cart functionality
    const removeFromCartButtons = document.querySelectorAll(".remove-from-cart-btn");
    removeFromCartButtons.forEach(button => {
        button.addEventListener("click", () => {
            const productName = button.getAttribute("data-product-name");

            fetch("/cart/remove", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ product_name: productName })
            })
                .then(response => response.json())
                .then(data => {
                    if (data.message) {
                        showToast(data.message);
                        updateCartCount(data.total_items);
                        updateCartUIAfterRemoval(button, data.total_price, data.total_items);
                    }
                })
                .catch(error => console.error("Error removing item from cart:", error));
        });
    });
}

/**
 * Set up event listeners for wishlist operations.
 */
function setupWishlistEventListeners() {
    // Add to wishlist functionality
    const addToWishlistButtons = document.querySelectorAll(".add-to-wishlist-btn");
    addToWishlistButtons.forEach(button => {
        button.addEventListener("click", () => {
            const productId = button.getAttribute("data-product-id");

            fetch("/wishlist/add", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ product_id: productId })
            })
                .then(response => response.json())
                .then(data => {
                    if (data.message) {
                        showToast(data.message);
                        updateWishlistCount(data.total_items);
                    }
                })
                .catch(error => console.error("Error adding item to wishlist:", error));
        });
    });

    // Remove from wishlist functionality
    const removeFromWishlistButtons = document.querySelectorAll(".remove-from-wishlist-btn");
    removeFromWishlistButtons.forEach(button => {
        button.addEventListener("click", () => {
            const productId = button.getAttribute("data-product-id");

            fetch("/wishlist/remove", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ product_id: productId })
            })
                .then(response => response.json())
                .then(data => {
                    if (data.message) {
                        showToast(data.message);
                        updateWishlistCount(data.total_items);
                        removeWishlistItem(button, data.total_items);
                    }
                })
                .catch(error => console.error("Error removing item from wishlist:", error));
        });
    });
}

/**
 * Set up event listener for placing an order.
 */
function setupOrderEventListener() {
    const placeOrderButton = document.getElementById("place-order-btn");
    if (placeOrderButton) {
        placeOrderButton.addEventListener("click", () => {
            const form = document.getElementById("shipping-form");
            if (form) {
                const formData = new FormData(form);
                const data = Object.fromEntries(formData.entries());

                fetch("/checkout", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(data)
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.message) {
                            alert(data.message);
                            window.location.href = "/checkout_success";
                        } else if (data.error) {
                            alert(data.error);
                        }
                    })
                    .catch(error => console.error("Error placing order:", error));
            }
        });
    }
}

/**
 * Function to display a toast notification.
 */
function showToast(message) {
    const toast = document.getElementById("toast-notification");
    const toastMessage = document.getElementById("toast-message");

    toastMessage.textContent = message;
    toast.classList.add("show");

    setTimeout(() => {
        toast.classList.remove("show");
    }, 3000);
}

/**
 * Autocomplete functionality for the search bar.
 */
function autocomplete(inp) {
    let currentFocus;

    inp.addEventListener("input", function () {
        const val = this.value;

        closeAllLists();
        if (!val) return;

        fetch(`/search/autocomplete?q=${encodeURIComponent(val)}`)
            .then(response => response.json())
            .then(arr => {
                createAutocompleteList(this, arr, val);
            })
            .catch(error => console.error("Autocomplete error:", error));
    });

    inp.addEventListener("keydown", function (e) {
        const x = document.getElementById(this.id + "autocomplete-list");
        if (x) var items = x.getElementsByTagName("div");

        if (e.keyCode == 40) {
            currentFocus++;
            addActive(items);
        } else if (e.keyCode == 38) {
            currentFocus--;
            addActive(items);
        } else if (e.keyCode == 13) {
            e.preventDefault();
            if (currentFocus > -1 && items) items[currentFocus].click();
        }
    });

    document.addEventListener("click", function (e) {
        closeAllLists(e.target);
    });

    function createAutocompleteList(input, suggestions, query) {
        const listContainer = document.createElement("div");
        listContainer.setAttribute("id", input.id + "autocomplete-list");
        listContainer.setAttribute("class", "autocomplete-items");

        suggestions.forEach(item => {
            const suggestion = document.createElement("div");
            suggestion.innerHTML = `<strong>${item.substr(0, query.length)}</strong>${item.substr(query.length)}`;
            suggestion.innerHTML += `<input type='hidden' value='${item}'>`;
            suggestion.addEventListener("click", () => {
                input.value = suggestion.getElementsByTagName("input")[0].value;
                closeAllLists();
            });
            listContainer.appendChild(suggestion);
        });

        input.parentNode.appendChild(listContainer);
    }

    function addActive(items) {
        if (!items) return;
        removeActive(items);
        if (currentFocus >= items.length) currentFocus = 0;
        if (currentFocus < 0) currentFocus = items.length - 1;
        items[currentFocus].classList.add("autocomplete-active");
    }

    function removeActive(items) {
        for (let i = 0; i < items.length; i++) {
            items[i].classList.remove("autocomplete-active");
        }
    }

    function closeAllLists(element) {
        const lists = document.getElementsByClassName("autocomplete-items");
        for (let i = 0; i < lists.length; i++) {
            if (element != lists[i] && element != inp) {
                lists[i].parentNode.removeChild(lists[i]);
            }
        }
    }
}

/**
 * Utility functions for UI updates.
 */
function updateCartCount(count) {
    const cartItemCount = document.getElementById("cart-item-count");
    if (cartItemCount) cartItemCount.textContent = count;
}

function updateWishlistCount(count) {
    const wishlistItemCount = document.getElementById("wishlist-item-count");
    if (wishlistItemCount) wishlistItemCount.textContent = count;
}

function updateCartUIAfterRemoval(button, totalPrice, totalItems) {
    const itemRow = button.closest("tr");
    if (itemRow) itemRow.remove();

    const totalPriceElement = document.getElementById("total-price");
    if (totalPriceElement) totalPriceElement.textContent = totalPrice.toFixed(2);

    if (totalItems === 0) {
        const cartContainer = document.querySelector(".cart-items-container");
        cartContainer.innerHTML = `<p>Your shopping cart is empty. <a href="/">Start shopping now!</a></p>`;
    }
}

function removeWishlistItem(button, totalItems) {
    const productElement = button.closest(".product");
    if (productElement) productElement.remove();

    if (totalItems === 0) {
        const wishlistContainer = document.querySelector(".wishlist-items-container");
        wishlistContainer.innerHTML = `<p>Your wishlist is empty. <a href="/">Start adding products now!</a></p>`;
    }
}
