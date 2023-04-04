<%@page import="Model.Bean.Admin"%>
<%@page import="Model.Bean.Trasua"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Cập nhật tai khoan</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <style>
        #main{
            display: flex;padding:20px;margin-top:180px;
        }
        #sidebar{
            width: 22%;
            height: 100%;
        }
        #content {
            width: 78%;
            height: 530px;
            border: 2px solid #007bff;
            padding: 10px 20px;
            margin-left:30px ;
            overflow-y: scroll;
        }
        #navbar{
            position: fixed;top: 0;width: 100%;height: 180px;z-index: 10;
        }
        <% if (request.getSession().getAttribute("account")==null) { %>
        .session {
        	display: none !important;
        }	
        <% } %>
        <% 
        if (request.getSession().getAttribute("account")!=null) {
        	if (!((Admin) request.getSession().getAttribute("account")).getRoles().equals("KH")) {
        %>
		        .sessionKH {
		        	display: none !important;
		        }	
        <% 
        	}
        } 
        %>
        <% 
        if (request.getSession().getAttribute("account")!=null) {
        	if (!((Admin) request.getSession().getAttribute("account")).getRoles().equals("AD")) {
        %>
		        .sessionAD {
		        	display: none !important;
		        }	
        <% 
        	}
        } 
        %>
    </style>
</head>
<body>
    <div id="navbar">
        <jsp:include page="Nav.jsp" ></jsp:include>
    </div>
    <div id="main">
        <div id="sidebar">
            <jsp:include page="Sidebar.jsp" ></jsp:include>
        </div>
        <div id="content" style="background-image: url('image/BG.png');">
            <section class="container wrapper" >
				<h2 class="display-6 pt-3">Cập Nhật</h2>
				<% 
				Admin khup = (Admin)request.getSession().getAttribute("account");
				%>
				<form action="Khachhang?updateexecute=1" method="POST" style="width:50%;margin:auto" >

					<input type="text" hidden required style="font-weight:bold" name="oldUserKH" id="oldUserKH" class="form-control" value="<%= khup.getUser() %>" >

                    <label for="user">Username</label>
					<input type="text" disabled required style="font-weight:bold" name="user" id="user" class="form-control" value="<%= khup.getUser() %>" >
					
                    <label for="pass">Password</label>
					<input type="text" required style="font-weight:bold" name="pass" id="pass" class="form-control" value="<%= khup.getPass() %>" >
					
                    <label for="firstname">Firstname</label>
					<input type="text" required style="font-weight:bold" name="firstname" id="firstname" class="form-control" value="<%= khup.getFirstname() %>">
					
					<label for="lastname">Lastname</label>
					<input type="text" required style="font-weight:bold" name="lastname" id="lastname" class="form-control" value="<%= khup.getLastname() %>">
					
					<label for="address">Address</label>
					<input type="text" required style="font-weight:bold" name="address" id="address" class="form-control" value="<%= khup.getAddress() %>">
					
					<label for="sdt">SDT</label>
					<input type="text" required style="font-weight:bold" name="sdt" id="sdt" class="form-control" value="<%= khup.getSdt() %>">
                    <br>
					
                    <input type="submit" id="ok" class="btn btn-block btn-outline-primary" value="OK" >
					<input type="reset" name="reset" id="res" class="btn btn-block btn-outline-primary" value="RESET">
				</form>
			</section>
        </div>
    </div>

</body>
</html>