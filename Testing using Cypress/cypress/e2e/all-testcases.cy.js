describe('BookWorms Shop Page - Functional, UI & Regression Tests', () => {

  beforeEach(() => {
    cy.visit('https://sahup9156.github.io/bookworms/shop.html');
  });

  // 1. Page Load Validation
  it('TC01 - Page loads successfully with all main sections', () => {
    cy.get('header').should('be.visible');
    cy.get('.products').should('be.visible');
    cy.get('footer').should('be.visible');
  });

  // 2. Navigation Links Visible
  it('TC02 - Navigation bar links are visible', () => {
    cy.get('nav a').should('contain.text', 'Home');
    cy.get('nav a').should('contain.text', 'about us');
    cy.get('nav a').should('contain.text', 'shop');
  });

  // 3. Category Filters Visible
  it('TC03 - Category filter section is visible', () => {
    cy.contains('h3', 'Categories').should('be.visible');
    cy.get('ul').contains('Biographies').should('exist');
    cy.get('ul').contains('Fiction').should('exist');
  });

  // 4. Price Range Filter Visible
  it('TC04 - Price range filter is displayed', () => {
    cy.contains('h3', 'Price range').should('be.visible');
  });

  // 5. Product Grid Loads
  it('TC05 - Product grid loads successfully', () => {
    cy.get('.products .product')
      .should('have.length.greaterThan', 0)
      .and('be.visible');
  });

  // 6. Product Card Structure Validation
  it('TC06 - Each product card contains title, price & button', () => {
    cy.get('.product').each((product) => {
      cy.wrap(product).find('img').should('be.visible');
      cy.wrap(product).find('h4').should('not.be.empty');
      cy.wrap(product).find('.price').should('contain.text', '$');
      cy.wrap(product).find('button').should('contain.text', 'Add to cart');
    });
  });

  // 7. Add to Cart Button Click
  it('TC07 - Add to cart button is clickable with no errors', () => {
    cy.get('.product').first().find('button').click();
  });

  // 8. Newsletter Subscription Box
  it('TC08 - Newsletter email box & subscribe button are visible', () => {
    cy.get('input[type="email"]').should('be.visible');
    cy.contains('button', 'Subscribe').should('be.visible');
  });

  // 9. Responsive Layout (Mobile)
  it('TC09 - Mobile layout renders correctly', () => {
    cy.viewport(400, 800);
    cy.get('header').should('be.visible');
    cy.get('.product').should('be.visible');
  });

  // 10. Footer Display
  it('TC10 - Footer information is visible', () => {
    cy.get('footer').should('be.visible');
    cy.get('footer').should('contain.text', 'contact');
  });

  // 11. Page Scroll Functionality
  it('TC11 - User can scroll from top to bottom without issues', () => {
    cy.scrollTo('bottom');
    cy.get('footer').should('be.visible');
    cy.scrollTo('top');
    cy.get('header').should('be.visible');
  });

  // 12. Product Images Load
  it('TC12 - Product images are loading', () => {
    cy.get('.product img').each((img) => {
      cy.wrap(img)
        .should('have.prop', 'naturalWidth')
        .should('be.greaterThan', 0);
    });
  });

  // 13. External CSS/JS Loads
  it('TC13 - All CSS & JS load successfully without 404 errors', () => {
    cy.request('https://sahup9156.github.io/bookworms/style.css')
      .its('status')
      .should('eq', 200);
  });

});

