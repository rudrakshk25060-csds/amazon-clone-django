// ============================================================
// script.js - Amazon Clone Simple Interactive JavaScript
// ============================================================

document.addEventListener('DOMContentLoaded', function () {

    // ────────────────────────────────────────────────────────
    // 1. ALL SIDE DRAWER MENU (Open, Close & Overlay)
    // ────────────────────────────────────────────────────────
    var openBtn = document.getElementById('open-sidebar-btn');
    var closeBtn = document.getElementById('close-sidebar-btn');
    var sidebarMenu = document.getElementById('sidebar-menu');
    var sidebarOverlay = document.getElementById('sidebar-overlay');

    // Function to open the sidebar drawer
    function openSidebar() {
        if (sidebarMenu && sidebarOverlay) {
            sidebarMenu.classList.add('active');
            sidebarOverlay.classList.add('active');
            document.body.style.overflow = 'hidden'; // Prevent page scrolling behind menu
        }
    }

    // Function to close the sidebar drawer
    function closeSidebar() {
        if (sidebarMenu && sidebarOverlay) {
            sidebarMenu.classList.remove('active');
            sidebarOverlay.classList.remove('active');
            document.body.style.overflow = ''; // Restore page scrolling
        }
    }

    // Event listener: clicking "☰ All" opens the menu
    if (openBtn) {
        openBtn.addEventListener('click', openSidebar);
    }

    // Event listener: clicking "X" closes the menu
    if (closeBtn) {
        closeBtn.addEventListener('click', closeSidebar);
    }

    // Event listener: clicking outside the menu (on the dark overlay) closes it
    if (sidebarOverlay) {
        sidebarOverlay.addEventListener('click', closeSidebar);
    }

    // Optional: Pressing Escape key closes the menu
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') {
            closeSidebar();
        }
    });

    // ────────────────────────────────────────────────────────
    // 2. BACK TO TOP BAR (Smooth Scroll to Top)
    // ────────────────────────────────────────────────────────
    var backToTopBar = document.getElementById('back-to-top-bar');
    if (backToTopBar) {
        backToTopBar.addEventListener('click', function () {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

});
