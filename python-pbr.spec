# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-pbr
Epoch: 100
Version: 5.10.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Python Build Reasonableness
License: Apache-2.0
URL: https://pypi.org/project/pbr/#history
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Manage dynamic plugins for Python applications.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pbr
Summary: Python Build Reasonableness
Requires: python3
Requires: python3-setuptools
Requires: python3-six
Provides: python3-pbr = %{epoch}:%{version}-%{release}
Provides: python3dist(pbr) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pbr = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pbr) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pbr = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pbr) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pbr
Manage dynamic plugins for Python applications.

%files -n python%{python3_version_nodots}-pbr
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-pbr
Summary: Python Build Reasonableness
Requires: python3
Requires: python3-setuptools
Requires: python3-six
Provides: python3-pbr = %{epoch}:%{version}-%{release}
Provides: python3dist(pbr) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pbr = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pbr) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pbr = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pbr) = %{epoch}:%{version}-%{release}

%description -n python3-pbr
Manage dynamic plugins for Python applications.

%files -n python3-pbr
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
