document.addEventListener("DOMContentLoaded", () => {
    // Add event listeners for adding to cart
    const addToCartButtons = document.querySelectorAll(".add-to-cart-btn");
    addToCartButtons.forEach(button => {
        button.addEventListener("click", () => {
            const productName = button.getAttribute("data-product-name");
            const quantityElement = button.parentElement.querySelector("input[name='quantity']");
            const quantity = quantityElement ? parseInt(quantityElement.value) : 1;

            // Make an AJAX request to add the product to the cart
            fetch("/cart/add", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    "product_name": productName,
                    "quantity": quantity
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    showToast(data.message); // Display the toast notification with the response message
                }

                // Update cart count
                const cartCountElement = document.querySelector("#cart-item-count");
                if (cartCountElement) {
                    cartCountElement.textContent = data.total_items;
                }
            })
            .catch(error => {
                console.error("Error adding item to cart:", error);
            });
        });
    });

    // Add event listeners for removing from cart
    const removeFromCartButtons = document.querySelectorAll(".remove-from-cart-btn");
    removeFromCartButtons.forEach(button => {
        button.addEventListener("click", () => {
            const productName = button.getAttribute("data-product-name");

            // Make an AJAX request to remove the product from the cart
            fetch("/cart/remove", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    "product_name": productName
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    showToast(data.message); // Display the toast notification with the response message
                }

                // Update cart count
                const cartCountElement = document.querySelector("#cart-item-count");
                if (cartCountElement) {
                    cartCountElement.textContent = data.total_items;
                }

                // Optionally, remove the row of the removed item from the cart page
                const itemRow = button.closest("tr");
                if (itemRow) {
                    itemRow.remove();
                }

                const totalPriceElement = document.querySelector("#total-price");
                if (totalPriceElement) {
                    totalPriceElement.textContent = data.total_price.toFixed(2);
                }

                // Check if the cart is empty and update the UI accordingly
                if (data.total_items === 0) {
                    const cartContainer = document.querySelector(".cart-items-container");
                    cartContainer.innerHTML = `
                        <p class="empty-cart-message">Your shopping cart is empty. <a href="/">Start shopping now!</a></p>
                    `;
                }
            })
            .catch(error => {
                console.error("Error removing item from cart:", error);
            });
        });
    });

    // Function to show a toast notification
    function showToast(message) {
        const toast = document.getElementById("toast-notification");
        const toastMessage = document.getElementById("toast-message");

        toastMessage.textContent = message;
        toast.classList.add("show");

        // Hide the toast after 3 seconds
        setTimeout(() => {
            toast.classList.remove("show");
        }, 3000);
    }
});

// Function to display flash messages dynamically
function displayFlashMessage(message, category) {
    let flashMessagesContainer = document.getElementById('flash-messages');
    if (!flashMessagesContainer) {
        flashMessagesContainer = document.createElement('div');
        flashMessagesContainer.id = 'flash-messages';
        flashMessagesContainer.classList.add('container', 'mt-3');
        document.body.prepend(flashMessagesContainer);
    }

    let alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${category}`;
    alertDiv.textContent = message;
    flashMessagesContainer.appendChild(alertDiv);

    // Remove the flash message after 3 seconds
    setTimeout(() => {
        alertDiv.style.transition = 'opacity 0.5s ease';
        alertDiv.style.opacity = '0';
        setTimeout(() => {
            alertDiv.remove();
        }, 500);
    }, 3000);
}

// Function to update the cart item count
function updateCartItemCount(count) {
    let cartItemCountElement = document.getElementById('cart-item-count');
    if (cartItemCountElement) {
        cartItemCountElement.textContent = count;
    }
}
