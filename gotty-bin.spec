%define _name gotty
%undefine _missing_build_ids_terminate_build

Name:		%{_name}-bin
Version:	1.0.1
Release:	1%{?dist}
Summary:	Share your terminal as a web application

Group:		Application/Utilities
License:	MIT
URL:		https://github.com/yudai/gotty
Source0:	https://github.com/yudai/gotty/releases/download/v%{version}/gotty_linux_amd64.tar.gz#/%{name}_linux_amd64-%{version}.tar.gz

%description
GoTTY is a simple command line tool that turns your CLI tools into web applications.

%prep
%setup -q -c %{name}-%{version}

%build


%install
install -d %{buildroot}/opt/%{_name}/bin
install %{_name} %{buildroot}/opt/%{_name}/bin/%{_name}

%files
/opt/%{_name}/bin/%{_name}
