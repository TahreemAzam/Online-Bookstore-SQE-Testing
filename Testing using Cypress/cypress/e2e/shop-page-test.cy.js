describe('BookWorms Shop Page', () => {
  beforeEach(() => {
    cy.visit('https://sahup9156.github.io/bookworms/shop.html');
  });
  //TC: 01 -------page loading------------
  it('TC01 - should load shop page and show title', () => {
    cy.get('h2').should('contain.text', 'world of reading');
  });
  //TC: 02 ------Shows navigation bar/link are visible or not -------
   it('TC02 - Navigation bar links are visible', () => {
    cy.get('nav a').should('contain.text', 'Home');
    cy.get('nav a').should('contain.text', 'about us');
    cy.get('nav a').should('contain.text', 'shop');
  });
  //TC: 03-------Filer section is visible or not------------------
  it('TC03 - Category filter section is visible', () => {
    cy.contains('h3', 'Categories').should('be.visible');
    cy.get('ul').contains('Biographies').should('exist');
    cy.get('ul').contains('Fiction').should('exist');
  });
  //Tc: 04---------Price range is visible or not -----------------
   it('TC04 - Price range filter is displayed', () => {
    cy.contains('h3', 'Price range').should('be.visible');
  });

});
