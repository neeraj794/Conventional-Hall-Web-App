document.addEventListener('DOMContentLoaded', ()=>{
    const mobMenu = document.getElementById('mobMenu')
    const mobNavbar = document.getElementById('mobNavbar')
    const mobNavbarCloseBtn = document.getElementById('mobNavbarCloseBtn')
    const addEvent = document.getElementById('addEvent')
    const deleteEvent = document.getElementById('deleteEvent')
    const modalOne = document.getElementById('modalOne')
    const closeModalOne = document.getElementById('closeModalOne')

    mobMenu.addEventListener('click', ()=>{
        mobNavbar.style.transform = 'translateX(0)'
    })
    mobNavbarCloseBtn.addEventListener('click', ()=>{
        mobNavbar.style.transform = 'translateX(100%)'
    })
    addEvent.addEventListener('click', ()=>{
        modalOne.style.display = 'flex'
        modalOne.style.justifyContent = 'space-evenly';
        modalOne.style.alignItem = 'center';
    })
    closeModalOne.addEventListener('click', ()=>{
        modalOne.style.display = ''
        modalOne.style.justifyContent = '';
        modalOne.style.alignItem = '';
    })
    

})